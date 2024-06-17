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
import xml.etree.ElementTree as ET
import pandas as pd


class JUnitSuite:
    """
    Class to represent a JUnit test suite.
    """
    def __init__(self, suite_et: ET.Element) -> None:
        """
        Initialize a JUnitSuite.

        Args:
            suite_et (Element): ElementTree element with the suite information.
        """
        self._suite_et = suite_et

    def to_df(self) -> pd.DataFrame:
        """
        Convert a JUnitSuit to a list of DataFrame entries.

        Returns:
            list: List of DataFrame entries.
        """
        df = pd.DataFrame()

        dataframe_entries = []
        timestamp = self._suite_et.attrib.get('timestamp')

        for testcase in self._suite_et.findall('.//testcase'):
            test_identifier = testcase.attrib.get('name')

            status = testcase.attrib.get('status')

            # Convert status to "pass" if it's "passed" or "run"
            if status == "passed" or status == "run":
                test_status = "pass"
            else:
                test_status = status
                if test_status == "skipped":
                    continue

            dataframe_entries.append(
                {
                    "timestamp": timestamp,
                    "test_identifier": test_identifier,
                    "test_status": test_status,
                }
            )

        if dataframe_entries:
            df = pd.DataFrame(dataframe_entries)
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df = df.set_index("timestamp")
            return df.sort_index()

        return df


class JUnitReport:
    """
    Class to represent a JUnit report.
    """
    def __init__(self, filename: str) -> None:
        """
        Initialize a JUnitReport.

        Args:
            filename (str): Path to the JUnit report file.
        """
        self._filename = filename
        self._suites = JUnitReport._get_suites(self._filename)

    def to_df(self) -> pd.DataFrame:
        """
        Convert a JUnitReport to a DataFrame.

        Returns:
            DataFrame: DataFrame with the report information.
        """
        df = pd.DataFrame()

        for suite in self._suites:
            df = pd.concat([df, suite.to_df()])

        return df

    @staticmethod
    def _get_suites(filename: str) -> list:
        """
        Get the suites from a JUnit report file.

        Args:
            filename (str): Path to the JUnit report file.

        Returns:
            list: List of JUnitSuite objects.
        """
        xml = ET.parse(filename)
        root = xml.getroot()

        # Root can be 'testsuites' or 'testsuite'
        suites = []
        if root.tag == 'testsuite':
            suites = [root]
        else:
            suites = root.findall('.//testsuite')

        return [JUnitSuite(suite) for suite in suites]
