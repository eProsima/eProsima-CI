# Copyright 2024 Proyectos y Sistemas de Mantenimiento SL (eProsima).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Script to parse the jUnit test results and create a summary."""

import argparse
import xml.etree.ElementTree as ET

DESCRIPTION = """Script to parse the jUnit test results and create a summary"""
USAGE = ('python3 junit_summary.py')


def parse_options():
    """
    Parse arguments.
    :return: The arguments parsed.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
        description=(DESCRIPTION),
        usage=(USAGE)
    )

    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument(
        '-j',
        '--junit-report',
        type=str,
        required=True,
        help='Path to junit report file.'
    )
    required_args.add_argument(
        '-o',
        '--output-file',
        type=str,
        required=True,
        help='Path to output file.'
    )
    parser.add_argument(
        '-p',
        '--print-summary',
        action='store_true',
        help='Print the summary to STDOUT'
    )
    parser.add_argument(
        '-f',
        '--show-failed',
        action='store_true',
        help='Show a list of failed tests'
    )
    parser.add_argument(
        '-d',
        '--show-disabled',
        action='store_true',
        help='Show a list of disabled tests'
    )
    parser.add_argument(
        '-s',
        '--show-skipped',
        action='store_true',
        help='Show a list of skipped tests'
    )

    return parser.parse_args()

def junit_report_to_dict(junit_report):
    """Convert a jUnit report to a dictionary."""
    result = []
    tree = ET.parse(junit_report)
    root = tree.getroot()

    # Root can be 'testsuites' or 'testsuite'
    if root.tag == 'testsuites':
        for test_suite in root:
            result = parse_testsuite(test_suite, result)
    elif root.tag == 'testsuite':
        result = parse_testsuite(root, result)

    return result


def parse_testsuite(test_suite, result):
    """Parse a testsuite tag."""
    suite_result = {
        'name': '',
        'tests': '',
        'failures': '',
        'time': '',
        'disabled': '',
        'skipped': '',
        'timestamp': '',
        'passed_tests': [],
        'failed_tests': [],
        'disabled_tests': [],
        'skipped_tests': []
    }

    suite_name = 'Not specified'
    if 'name' in test_suite.attrib and test_suite.attrib['name'] != '(empty)':
        suite_name = test_suite.attrib['name']

    suite_result['name'] = suite_name
    suite_result['tests'] = test_suite.attrib['tests']
    suite_result['failures'] = test_suite.attrib['failures']
    suite_result['time'] = test_suite.attrib['time']

    suite_result['disabled'] = None
    if 'disabled' in test_suite.attrib:
        suite_result['disabled'] = test_suite.attrib['disabled']

    suite_result['skipped'] = None
    if 'skipped' in test_suite.attrib:
        suite_result['skipped'] = test_suite.attrib['skipped']

    suite_result['timestamp'] = None
    if 'timestamp' in test_suite.attrib:
        suite_result['timestamp'] = test_suite.attrib['timestamp']

    for child in test_suite:
        if child.tag == 'testcase':
            if child.attrib['status'] == "run" or child.attrib['status'] == "passed":
                suite_result['passed_tests'].append(child.attrib['name'])

            elif child.attrib['status'] == "fail" or child.attrib['status'] == "failed":
                suite_result['failed_tests'].append(child.attrib['name'])

            elif child.attrib['status'] == "ignored":
                suite_result['disabled_tests'].append(child.attrib['name'])

            elif child.attrib['status'] == "notrun":
                suite_result['skipped_tests'].append(child.attrib['name'])

    result.append(suite_result)

    return result

def create_md_summary(results, show_failed, show_disabled, show_skipped):
    """Create Markdown summary from results."""
    # Test summary
    summary = '## Test summary\n'

    # Table header
    summary += '|Suite|Total number of tests|Test failures|Disabled test|Skipped test|Spent time [s]|Timestamp|\n'
    summary += '|-|-|-|-|-|-|-|\n'

    # Entries
    for suite in results:
        summary += f'|{suite["name"]}'
        summary += f'|{suite["tests"]}'
        summary += f'|{suite["failures"]}'
        summary += f'|{suite["disabled"]}'
        summary += f'|{suite["skipped"]}'
        summary += f'|{suite["time"]}'
        summary += f'|{suite["timestamp"]}'
        summary += '|\n'

    # Test lists
    for suite in results:
        # Failed tests list
        if show_failed is True and len(suite['failed_tests']) != 0:
            summary += f'\n### Suite `{suite["name"]}` had {suite["failures"]} failed tests:\n'
            summary += '<details>\n\n'
            for failed_test in suite['failed_tests']:
                summary += f'* {failed_test}\n'
            summary += '</details>\n'

        # Disabled tests list
        if show_disabled is True and len(suite['disabled_tests']) != 0:
            summary += f'\n### Suite `{suite["name"]}` had {suite["disabled"]} disabled tests:\n'
            summary += '<details>\n'
            for failed_test in suite['disabled_tests']:
                summary += f'* {failed_test}\n'
            summary += '</details>\n'

        # Skipped tests list
        if show_skipped is True and len(suite['skipped_tests']) != 0:
            summary += f'\n### Suite `{suite["name"]}` had {suite["skipped"]} skipped tests:\n'
            summary += '<details>\n\n'
            for failed_test in suite['skipped_tests']:
                summary += f'* {failed_test}\n'
            summary += '</details>\n'

    return summary


if __name__ == '__main__':
    # Parse arguments
    args = parse_options()
    results = junit_report_to_dict(args.junit_report)

    # Create summary
    summary = create_md_summary(
        results,
        args.show_failed,
        args.show_disabled,
        args.show_skipped
    )

    # Print summary if required
    if args.print_summary is True:
        print(summary)

    # Write output if required
    if args.output_file != '':
        with open(args.output_file, 'a') as file:
            file.write(summary)

    # Exit code is the number of failed tests
    exit_code = 0
    for suite in results:
        exit_code += int(suite['failures'])
    exit(exit_code)
