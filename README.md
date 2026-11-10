# Jenkins CI Assignment: Student-CI-Project

A small Python calculator application with automated tests, built and tested
by the Jenkins Freestyle job `Student-CI-Project`, which is triggered by a GitHub webhook.

CMSC-426-001, In-Class Activity 3: *Building an Automated CI Pipeline Using Jenkins and GitHub*.

## Repository layout

```
app/calculator.py        Application code (add, subtract, multiply, divide, power)
tests/test_calculator.py unittest test cases
tests/run_tests.py       Test runner that also writes reports/junit.xml for Jenkins
ci/build.sh              Build script run by the Jenkins job
```

## Requirements

* Python 3.8 or newer (standard library only)
* Jenkins LTS with the Git, GitHub and JUnit plugins
* Git

## Run locally

```sh
python3 -m app.calculator           # run the application
python3 -m unittest discover -s tests -t .   # run the tests
./ci/build.sh                       # run exactly what Jenkins runs
```

`ci/build.sh` exits with code `0` when every test passes and `1` when any step
fails, which is what makes Jenkins mark the build as FAILURE.

## Jenkins job configuration

* **Source Code Management:** Git, `https://github.com/RDaou05/Jenkins-assignment.git`, branch `*/main`
* **Build Triggers:** *GitHub hook trigger for GITScm polling*, plus *Poll SCM* `H/5 * * * *` as a fallback
* **Build step:** *Execute shell* `./ci/build.sh`
* **Post-build action:** *Publish JUnit test result report* `reports/junit.xml`

The GitHub webhook points to `https://<ngrok-host>/github-webhook/`, uses content type
`application/json` and a shared secret, and sends push events.
