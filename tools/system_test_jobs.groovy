// This file is used to generate the system_tests jobs. There will be one job per driver per bitness.
// See https://github.com/ni/nimi-python/wiki/nimi-bot-separate-server-and-agents (this location will change
// once the documentation is finalized)

// Driver list
DRIVERS = [ "nidcpower", "nidigital", "nidmm", "nifgen", "niscope", "niswitch", "nise", "nimodinst" ]
// Platform list - also used as node label
PLATFORMS = [ "win32", "win64" ]

ROOT_FOLDER = "nimi-bot"
credentials_to_use = 'c07926b1-d626-4476-892a-e21bb6d28733'  // nimi-bit username/PAT

// This function generates a job for the given driver and platform
// returns generatd job name
def genJob(driver, platform) {
    jobName = "${ROOT_FOLDER}/${platform}/${driver}"
    println "Processing ${jobName}"
    job("${jobName}") {
        description "Run system tests for ${driver} on ${platform}"

        label(platform)

        parameters {
            stringParam('sha1', 'master', 'SHA to build')
        }

        scm {
            git {
                extensions {
                    wipeWorkspace()
                }
                branch('${sha1}')
                remote {
                    github('ni/nimi-python')
                    credentials("${credentials_to_use}")
                    refspec('+refs/pull/${ghprbPullId}/*:refs/remotes/origin/pr/${ghprbPullId}/*')
                    name('origin')
                }
            }
        }

        triggers {
            githubPullRequest {
                admins(['texasaggie97', 'marcoskirsch', 'sbethur'])
                userWhitelist(['injaleea', 'bhaswath', 'AlexHearnNI'])
                orgWhitelist('ni')
                extensions {
                    commitStatus {
                        context("system_tests/jenkins/${platform}/${driver}")
                        triggeredStatus("${platform}/${driver} triggered...")
                        startedStatus("${platform}/${driver} running...")
                        addTestResults(true)
                        completedStatus('SUCCESS', "Passed!")
                        completedStatus('FAILURE', "Failure!")
                        completedStatus('ERROR', "Error!")
                    }
                }
            }
        }

        // Once we add automated system tests on Linux, we will need to generate the steps differently
        steps {
            batchFile {
                command("""@echo off
echo Running system tests for ${driver} on ${platform}
tools\\system_tests.bat ${driver}
""")
            }
        }

        publishers {
            archiveJunit("generated/junit/*.xml") {
                retainLongStdout()
            }
        }
    }

    return jobName
}

// Make sure the folders exist to organize the jobs
folder("${ROOT_FOLDER}")
for (platform in PLATFORMS)
{
    folder("${ROOT_FOLDER}/${platform}")
}

jobList = []
for (driver in DRIVERS)
{
    for (platform in PLATFORMS)
    {
        jobName = genJob(driver, platform)
        jobList.add(jobName)
    }
}

// Generate the trigger job
job("${ROOT_FOLDER}/Trigger") {
    description "Run all driver system tests on all platforms"

    parameters {
        stringParam('sha1', 'master', 'SHA to build')
    }

    label('master')

    scm {
        git {
            extensions {
                wipeWorkspace()
            }
            branch('${sha1}')
            remote {
                github('ni/nimi-python')
                credentials("${credentials_to_use}")
                refspec('+refs/pull/${ghprbPullId}/*:refs/remotes/origin/pr/${ghprbPullId}/*')
                name('origin')
            }
        }
    }

    steps {
        batchFile {
            command("echo Starting system tests")
        }
    }

    triggers {
        githubPullRequest {
            admins(['texasaggie97', 'marcoskirsch', 'sbethur'])
            userWhitelist(['injaleea', 'bhaswath', 'AlexHearnNI'])
            orgWhitelist('ni')
            cron('H/5 * * * *')
            extensions {
                commitStatus {
                    context('system_tests/jenkins/start')
                    triggeredStatus('starting system tests')
                    startedStatus('start system tests')
                    completedStatus('SUCCESS', 'All system test jobs queued')
                    completedStatus('FAILURE', 'Failure starting system tests')
                    completedStatus('ERROR', 'Error starting system tests')
                }
            }
        }
    }

    publishers {
        downstreamParameterized {
            trigger(jobList) {
                condition('UNSTABLE_OR_BETTER')
                parameters {
                    predefinedProp('sha1', '${sha1}')
                }
            }
        }
    }
}

