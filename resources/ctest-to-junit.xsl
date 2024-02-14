<?xml version="1.0" encoding="UTF-8"?>
<!-- Taken from https://github.com/rpavlik/jenkins-ctest-plugin/blob/master/ctest-to-junit.xsl -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes" />
    <xsl:template match="/">
        <testsuites>
            <xsl:variable name="buildName" select="//Site/@BuildName"/>
            <xsl:variable name="numberOfTests" select="count(//Site/Testing/Test)"/>
            <xsl:variable name="numberOfFailures" select="count(//Site/Testing/Test[@Status='failed'])" />
            <xsl:variable name="numberOfErrors" select="count(//Site/Testing/Test[@Status='error'])" />
            <xsl:variable name="numberOfSkipped" select="count(//Site/Testing/Test[@Status='notrun'])"/>
            <xsl:variable name="buildTime" select="(//Site/Testing/EndTestTime - //Site/Testing/StartTestTime)"/>
            <testsuite name="CTest"
                tests="{$numberOfTests}"
                failures="{$numberOfFailures}"
                errors="{$numberOfErrors}"
                skipped="{$numberOfSkipped}"
                time="{$buildTime}">
            <xsl:for-each select="//Site/Testing/Test">
                    <xsl:variable name="testName" select="translate(Name, '-', '_')"/>
                    <xsl:variable name="duration" select="Results/NamedMeasurement[@name='Execution Time']/Value"/>
                    <xsl:variable name="status" select="@Status"/>
                    <xsl:variable name="output" select="Results/Measurement/Value"/>
                    <xsl:variable name="className" select="translate(Path, '/.', '.')"/>
                    <testcase classname="projectroot{$className}"
                        name="{$testName}"
                        status="{$status}"
                        time="{$duration}">
                        <xsl:if test="@Status!='passed'">
                            <failure>
                                <xsl:value-of select="$output" />
                            </failure>
                        </xsl:if>
                        <system-out>
                            <xsl:value-of select="$output" />
                        </system-out>
                    </testcase>
                </xsl:for-each>
            </testsuite>
        </testsuites>
    </xsl:template>
</xsl:stylesheet>
