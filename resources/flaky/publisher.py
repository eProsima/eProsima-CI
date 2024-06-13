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
import json
from decimal import Decimal

from flaky.archive import FlakyTestsArchive


class FlakyTestsMdPublisher:
    """
    Class to publish FlakyTestsArchive as a markdown file.
    """
    @staticmethod
    def publish(test_archive: FlakyTestsArchive, output_file: str) -> None:
        """
        Publish the FlakyTestsArchive to a markdown file.

        Args:
            test_archive (FlakyTestsArchive): Archive with the flaky tests.
            output_file (str): Path to the output file.
        """
        # Test report
        report = '## Flaky tests\n'

        # Table header
        # TODO(eduponz): Add a column for the failures/runs ratio
        report += '|#|Flaky tests|Fliprate score %|Consecutive failures|Consecutive passes|Total failures|\n'
        report += '|-|-|-|-|-|-|\n'

        analysis = dict(test_archive)
        assert(analysis['version'] == '1.0')

        i = 1
        for test_name, result in analysis['flaky_tests'].items():
            report += f'| {i} '
            report += f'| {test_name} '
            report += f'| {round(result["flip_rate"], 2) * 100} '
            report += f'| {result["consecutive_failures"]} '
            report += f'| {result["consecutive_passes"]} '
            report += f'| {result["failures"]} |\n'
            i += 1

        with open(output_file, 'w') as file:
            file.write(report)


class FlakyTestsJSONPublisher:
    """
    Class to publish FlakyTestsArchive as a JSON file.
    """

    @staticmethod
    def publish(test_archive: FlakyTestsArchive, output_file: str) -> None:
        """
        Publish the FlakyTestsArchive to a JSON file.

        Args:
            test_archive (FlakyTestsArchive): Archive with the flaky tests.
            output_file (str): Path to the output file.
        """
        analysis = dict(test_archive)

        with open(output_file, 'w') as file:
            json.dump(analysis, file, indent=4, cls=_CustomEncoder)


class _CustomEncoder(json.JSONEncoder):
    """
    Custom JSON encoder with support for Decimal objects.
    """
    def default(self, o: object) -> str:
        """
        Encode the object.

        Args:
            o: Object to encode.

        Returns:
            str: Encoded object.
        """
        # Encode Decimal objects as strings with 2 decimal places
        if isinstance(o, Decimal):
            return f'{o:.2f}'

        # Leave the rest to the default encoder
        return super(_CustomEncoder, self).default(o)
