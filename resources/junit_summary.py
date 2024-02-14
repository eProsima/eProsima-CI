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
    result = {}
    tree = ET.parse(junit_report)
    root = tree.getroot()
    print(root)
    print(root.tag)

    # Root can be 'testsuites' or 'testsuite'
    if root.tag == 'testsuites':
        for test_suite in root:
            result = parse_testsuite(test_suite, result)
    elif root.tag == 'testsuite':
        print('parsing testsuite')
        result = parse_testsuite(root, result)

    print(result)
    return result


def parse_testsuite(test_suite, result):
    """Parse a testsuite tag."""
    suite_result = {
        'passed_tests': [],
        'failed_tests': [],
        'disabled_tests': [],
        'skipped_tests': [],
    }
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

    # Update result
    suite_name = 'Not specified'
    if 'name' in test_suite.attrib and test_suite.attrib['name'] != '(empty)':
        suite_name = test_suite.attrib['name']
    result[suite_name] = suite_result

    return result

def create_md_summary(results_dict, show_failed, show_disabled, show_skipped):
    """Create Markdown summary from results."""
    # Test summary
    summary = '## Test summary\n'

    # Table header
    summary += '|Suite|Total number of tests|Test failures|Disabled test|Skipped test|Spent time [s]|Timestamp|\n'
    summary += '|-|-|-|-|-|-|-|\n'

    # Entries
    for suite, suite_results in results_dict.items():
        summary += f'|{suite}'
        summary += f'|{suite_results["tests"]}'
        summary += f'|{suite_results["failures"]}'
        summary += f'|{suite_results["disabled"]}'
        summary += f'|{suite_results["skipped"]}'
        summary += f'|{suite_results["time"]}'
        summary += f'|{suite_results["timestamp"]}'
        summary += '|\n'

    # Test lists
    for suite, suite_results in results_dict.items():
        # Failed tests list
        if show_failed is True and len(suite_results['failed_tests']) != 0:
            summary += f'\n## Failed tests in suite: {suite}\n'
            for failed_test in suite_results['failed_tests']:
                summary += f'* {failed_test}\n'

        # Disabled tests list
        if show_disabled is True and len(suite_results['disabled_tests']) != 0:
            summary += f'\n## Disabled tests in suite: {suite}\n'
            for failed_test in suite_results['disabled_tests']:
                summary += f'* {failed_test}\n'

        # Skipped tests list
        if show_skipped is True and len(suite_results['skipped_tests']) != 0:
            summary += f'\n## Skipped tests in suite: {suite}\n'
            for failed_test in suite_results['skipped_tests']:
                summary += f'* {failed_test}\n'

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
            file.write(
                create_md_summary(
                    results,
                    args.show_failed,
                    args.show_disabled,
                    args.show_skipped
                )
            )

    # Exit code is the number of failed tests
    exit_code = 0
    for suite in results:
        exit_code += int(results[suite]['failures'])
    exit(exit_code)
