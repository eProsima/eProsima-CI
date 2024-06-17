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
import json
import xml.etree.ElementTree as ET

DESCRIPTION = """Script to parse the jUnit test results and create a summary"""
USAGE = ('python3 junit_summary.py')


def parse_options() -> argparse.Namespace:
    """
    Parse arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
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
    parser.add_argument(
        '--flaky-json-report',
        type=str,
        required=False,
        help='Path to flaky json report file'
    )

    return parser.parse_args()

def junit_report_to_dict(junit_report: str) -> list:
    """
    Parse a junit report to a dictionary.

    Args:
        junit_report (str): Path to junit report.

    Returns:
        list: List of dictionaries with the parsed information.
    """
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


def parse_testsuite(test_suite: ET.Element, result: list) -> list:
    """
    Parse a test suite tag.

    Args:
        test_suite (Element): Element with the test suite information.
        result (list): List with the parsed information.

    Returns:
        list: List with the parsed information.
    """
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

def create_md_summary(
        results: list,
        show_failed: bool,
        show_disabled: bool,
        show_skipped: bool,
        flaky_tests: list
    ) -> str:
    """
    Create Markdown summary from results.

    Args:
        results (list): List of dictionaries with the parsed information.
        show_failed (bool): Show failed tests.
        show_disabled (bool): Show disabled tests.
        show_skipped (bool): Show skipped tests.
        flaky_tests (list): List of flaky tests.

    Returns:
        str: Markdown summary.
    """
    flaky_failures = 0
    if len(flaky_tests) != 0:
        for suite in results:
            for failed_test in suite['failed_tests']:
                if failed_test in flaky_tests:
                    flaky_failures += 1

    # Test summary
    summary = '## Test summary\n'

    # Table header
    summary += '|Suite'
    summary += '|Total number of tests'
    summary += '|Test failures'
    summary += '|Disabled test'
    summary += '|Skipped test'
    summary += '|Flaky failures'
    summary += '|Spent time [s]'
    summary += '|Timestamp'
    summary += '|\n'
    summary += '|-|-|-|-|-|-|-|-|\n'

    # Entries
    for suite in results:
        summary += f'|{suite["name"]}'
        summary += f'|{suite["tests"]}'
        summary += f'|{suite["failures"]}'
        summary += f'|{suite["disabled"]}'
        summary += f'|{suite["skipped"]}'
        summary += f'|{flaky_failures}'
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


def get_flaky_tests(flaky_json_report: str) -> list:
    """
    Get flaky tests from a flaky json report.

    Args:
        flaky_json_report (str): Path to flaky json report.

    Returns:
        list: List of flaky tests. Empty list if no flaky tests found.
    """
    flaky_tests = []
    try:
        with open(flaky_json_report, 'r') as file:
            flaky_json = json.load(file)
            if 'version' in flaky_json and flaky_json['version'] == '1.0':
                assert('flaky_tests' in flaky_json)
                assert(type(flaky_json['flaky_tests']) == dict)
                flaky_tests = list(flaky_json['flaky_tests'].keys())
    except FileNotFoundError:
        pass

    return flaky_tests


if __name__ == '__main__':
    # Parse arguments
    args = parse_options()

    # Parse junit report
    results = junit_report_to_dict(args.junit_report)

    # Get flaky tests names
    flaky_tests = []
    if args.flaky_json_report:
        flaky_tests = get_flaky_tests(args.flaky_json_report)

    # Create summary
    summary = create_md_summary(
        results,
        args.show_failed,
        args.show_disabled,
        args.show_skipped,
        flaky_tests
    )

    # Print summary if required
    if args.print_summary is True:
        print(summary)

    # Write output if required
    if args.output_file != '':
        with open(args.output_file, 'a') as file:
            file.write(summary)

    # Exit code is the number of non-flaky failed tests
    exit_code = 0
    for suite in results:
        for failed_test in suite['failed_tests']:
            if failed_test not in flaky_tests:
                exit_code += 1

    exit(exit_code)
