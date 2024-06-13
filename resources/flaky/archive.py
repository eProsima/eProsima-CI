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
import os
import re
from datetime import datetime
from decimal import getcontext, Decimal, ROUND_UP

import pandas as pd

from junit.junit_utils import JUnitReport


class FlakyTestsArchive:
    """
    Class to analyze and store flaky tests from JUnit test history files.
    """
    # Regex pattern to match the timestamp part of the filename
    _timestamp_rstr = r'\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}'

    def __init__(self, archive_dir: str, window_size: int, delete_old_files: bool = True) -> None:
        """
        Args:
            archive_dir (str): Path to the directory containing the JUnit test history files.
            window_size (int): Number of test runs to consider for the fliprate calculation.
            delete_old_files (bool): Whether to delete old files taking window_size into account.
        """
        self._analysis = {
            'version': '1.0',
            'flaky_tests': {},
            'failed_tests': {},
        }
        self._window_size = window_size
        self._junit_files = FlakyTestsArchive._find_test_results(archive_dir)

        if delete_old_files:
            self._delete_old_files()

        self._analyze()

    def _analyze(self) -> None:
        """
        Analyze the test history files and calculate the fliprate for each test.

        Returns:
            int: Number of flaky tests found.
        """
        df = pd.DataFrame()
        for junit_file in self._junit_files:
            junit_report = JUnitReport(junit_file)
            df = pd.concat([df, junit_report.to_df()])

        fliprate_table = FlakyTestsArchive._calculate_fliprate_table(df, self._window_size)
        self._get_top_fliprates(fliprate_table, 0, 4)

    @property
    def flaky_test_count(self) -> int:
        return len(self._analysis)

    @staticmethod
    def _find_test_results(directory: str) -> list:
        """
        Find all JUnit test history files in the given directory.

        Args:
            directory (str): Path to the directory containing the JUnit test history files.

        Returns:
            list: List of paths to the JUnit test history files.
        """
        pattern = re.compile(r'^.*test_results.*' + FlakyTestsArchive._timestamp_rstr + r'\.xml$')

        files = os.listdir(directory)
        matched_files = [
            os.path.join(directory, f) for f in files if pattern.match(f)
        ]
        matched_files.sort(key=FlakyTestsArchive._extract_timestamp)

        return matched_files

    @staticmethod
    def _extract_timestamp(file_path: str) -> datetime:
        """
        Extract the timestamp from the filename.

        Args:
            file_path (str): Path to the file.

        Returns:
            datetime: Timestamp extracted from the filename.
        """
        filename = os.path.basename(file_path)
        timestamp_str = re.search(FlakyTestsArchive._timestamp_rstr, filename).group()
        return datetime.strptime(timestamp_str, '%Y-%m-%dT%H-%M-%S')

    def _delete_old_files(self) -> None:
        """
        Delete old files taking window_size into account.
        """
        if len(self._junit_files) > self._window_size:
            # Calculate the number of files to delete
            files_to_delete = self._junit_files[:-self._window_size]

            # Update the list of kept files
            self._junit_files = self._junit_files[-self._window_size:]

            # Delete the older files
            for file in files_to_delete:
                print(f'Deleting old file: {file}')
                os.remove(file)

    @staticmethod
    def _calculate_fliprate_table(testrun_table: pd.DataFrame, window_size: int) -> pd.DataFrame:
        """
        Calculate the fliprate for each test in the testrun_table.

        Args:
            testrun_table (pd.DataFrame): DataFrame with the test results.
            window_size (int): Number of test runs to consider for the fliprate calculation.

        Returns:
            pd.DataFrame: DataFrame with the fliprates for each test.
        """
        # Apply non_overlapping_window_fliprate to each group in testrun_table
        fliprates = testrun_table.groupby("test_identifier")["test_status"].apply(
            lambda x: FlakyTestsArchive._non_overlapping_window_fliprate(x, window_size)
        )

        # Convert fliprates Series of DataFrames to a DataFrame
        fliprate_table = fliprates.reset_index()

        # Rename the index level to "window"
        fliprate_table = fliprate_table.rename(columns={"level_1": "window"})

        # Filter out rows where flip_rate is zero
        # TODO(eduponz): I'm seeing tests with 5 consecutive failures that are not showing here.
        #                Seems it's because they are not flaky, they are just always failing.
        fliprate_table = fliprate_table[fliprate_table.flip_rate != 0]

        return fliprate_table

    @staticmethod
    def _non_overlapping_window_fliprate(testruns: pd.Series, window_size: int) -> pd.Series:
        """
        Calculate the fliprate for a test in a non-overlapping window.

        Args:
            testruns (pd.Series): Series with the test results.
            window_size (int): Number of test runs to consider for the fliprate calculation.

        Returns:
            pd.Series: Series with the fliprate for the test.
        """
        # Apply _calc_fliprate directly to the last <window_size> selected rows
        testruns_last = testruns.iloc[-window_size:]
        fliprate_groups = FlakyTestsArchive._calc_fliprate(testruns_last)

        return fliprate_groups.reset_index(drop=True)

    @staticmethod
    def _calc_fliprate(testruns: pd.Series) -> pd.DataFrame:
        """
        Calculate the fliprate for a test.

        Args:
            testruns (pd.Series): Series with the test results.

        Returns:
            pd.DataFrame: DataFrame with the fliprate, consecutive failures
                          and consecutive passes for the test.
        """
        if len(testruns) < 2:
            return pd.DataFrame(
                {
                    'flip_rate': [0.0],
                    'consecutive_failures': [0],
                    'consecutive_passes': [0],
                    'failures': [0],
                }
            )

        first = True
        previous = None
        flips = 0
        consecutive_failures = 0
        consecutive_passes = 0
        failures = 0
        possible_flips = len(testruns) - 1

        for _, val in testruns.items():
            if first:
                first = False
                previous = val
                continue

            if val != previous:
                flips += 1

            if val != "pass":
                consecutive_failures += 1
                consecutive_passes = 0
                failures += 1
            else:
                consecutive_failures = 0
                consecutive_passes += 1

            previous = val

        flip_rate = flips / possible_flips

        return pd.DataFrame(
            {
                'flip_rate': [flip_rate],
                'consecutive_failures': [consecutive_failures],
                'consecutive_passes': [consecutive_passes],
                'failures': [failures],
            }
        )

    def _get_top_fliprates(self, fliprate_table: pd.DataFrame, top_n: int, precision: int) -> None:
        """
        Get the top N fliprates from the fliprate_table.

        Args:
            fliprate_table (pd.DataFrame): DataFrame with the fliprates.
            top_n (int): Number of top fliprates to get.
            precision (int): Number of decimal places to round the fliprates.
        """
        context = getcontext()
        context.prec = precision
        context.rounding = ROUND_UP
        last_window_values = fliprate_table.groupby("test_identifier").last()

        if top_n != 0:
            top_fliprates = last_window_values.nlargest(top_n, "flip_rate")
        else :
            top_fliprates = last_window_values.nlargest(len(last_window_values), "flip_rate")

        # Create a dictionary with test_identifier as keys and a tuple of flip_rate and consecutive_failures as values
        results = {}
        for test_id, row in top_fliprates.iterrows():
            results[test_id] = {
                'flip_rate': Decimal(row['flip_rate']),
                'consecutive_failures': int(row['consecutive_failures']),
                'consecutive_passes': int(row['consecutive_passes']),
                'failures': int(row['failures'])
            }

        self._analysis['flaky_tests'] = results

    def __getitem__(self, key: str) -> any:
        """
        Get the value for the given key.

        Args:
            key: Key to get the value for.

        Returns:
            Any: Value for the given key.
        """
        return self._analysis[key]

    def __iter__(self) -> iter:
        """
        Return an iterator over the FlakyTestsArchive.

        Returns:
            iter: Iterator over the FlakyTestsArchive.
        """
        return iter(self._analysis)

    def items(self) -> dict:
        """
        Return the FlakyTestsArchive as a dictionary.

        Returns:
            dict: FlakyTestsArchive as a dictionary.
        """
        return self._analysis.items()

    def keys(self) -> list:
        """
        Return the keys of the FlakyTestsArchive.

        Returns:
            list: Keys of the FlakyTestsArchive.
        """
        return self._analysis.keys()

    def values(self) -> list:
        """
        Return the values of the FlakyTestsArchive.

        Returns:
            list: Values of the FlakyTestsArchive.
        """
        return self._analysis.values()

    def __dict__(self) -> dict:
        """
        Return the FlakyTestsArchive as a dictionary.
        """
        return self._analysis
