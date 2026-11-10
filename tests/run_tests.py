"""Run the unittest suite and write a JUnit XML report for Jenkins.

Uses only the standard library so the build needs no extra packages.
Exit code is 0 when every test passes and 1 otherwise.
"""
import os
import sys
import time
import unittest
import xml.etree.ElementTree as ET


class RecordingResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []
        self._start = 0.0

    def startTest(self, test):
        self._start = time.perf_counter()
        super().startTest(test)

    def _record(self, test, outcome, detail=""):
        elapsed = time.perf_counter() - self._start
        self.records.append((test, outcome, detail, elapsed))

    def addSuccess(self, test):
        super().addSuccess(test)
        self._record(test, "passed")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self._record(test, "failure", self._exc_info_to_string(err, test))

    def addError(self, test, err):
        super().addError(test, err)
        self._record(test, "error", self._exc_info_to_string(err, test))

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self._record(test, "skipped", reason)


def write_junit(result, path, total_time):
    suite = ET.Element(
        "testsuite",
        name="calculator-tests",
        tests=str(result.testsRun),
        failures=str(len(result.failures)),
        errors=str(len(result.errors)),
        skipped=str(len(result.skipped)),
        time=f"{total_time:.3f}",
    )
    for test, outcome, detail, elapsed in result.records:
        test_id = test.id()
        classname, _, name = test_id.rpartition(".")
        case = ET.SubElement(
            suite, "testcase", classname=classname, name=name, time=f"{elapsed:.3f}"
        )
        if outcome in ("failure", "error"):
            child = ET.SubElement(case, outcome, message=detail.strip().splitlines()[-1])
            child.text = detail
        elif outcome == "skipped":
            ET.SubElement(case, "skipped", message=detail)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    ET.ElementTree(suite).write(path, encoding="utf-8", xml_declaration=True)


def main():
    # Running "python tests/run_tests.py" puts tests/ on sys.path, not the
    # project root, so make the app package importable explicitly.
    sys.path.insert(0, os.getcwd())
    report_path = os.path.join("reports", "junit.xml")
    suite = unittest.defaultTestLoader.discover("tests", top_level_dir=".")
    runner = unittest.TextTestRunner(verbosity=2, resultclass=RecordingResult)
    start = time.perf_counter()
    result = runner.run(suite)
    write_junit(result, report_path, time.perf_counter() - start)
    print(f"JUnit report written to {report_path}")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
