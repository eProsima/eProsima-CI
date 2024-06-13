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
"""
Script to analyze and publish flaky tests from JUnit test history files.
"""
import argparse

from flaky.archive import FlakyTestsArchive
from flaky.publisher import FlakyTestsMdPublisher
from flaky.publisher import FlakyTestsJSONPublisher

def parse_options() -> argparse.Namespace:
    """
    Parse the command line options.

    Returns:
        argparse.Namespace: Parsed command line options.
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--junit-archive",
        help="Path for a folder with JUnit xml test history files",
        type=str
    )
    parser.add_argument(
        "--window-size",
        type=int,
        help="flip rate calculation window size",
        required=True,
    )
    parser.add_argument(
        '-d',
        '--delete-old-files',
        action='store_true',
        help='Delete old files taking window size into account.'
    )
    parser.add_argument(
        '-m',
        '--markdown-file',
        type=str,
        required=False,
        help='Path to markdown file.'
    )
    parser.add_argument(
        '-j',
        '--json-file',
        type=str,
        required=False,
        help='Path to JSON file.'
    )
    return parser.parse_args()

if __name__ == "__main__":

    args = parse_options()

    archive = FlakyTestsArchive(
        args.junit_archive,
        args.window_size,
        args.delete_old_files
    )

    if args.markdown_file:
        FlakyTestsMdPublisher.publish(archive, args.markdown_file)

    if args.json_file:
        FlakyTestsJSONPublisher.publish(archive, args.json_file)

    ret = 0 if archive.flaky_test_count == 0 else 1
    exit(ret)
