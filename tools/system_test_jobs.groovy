// This file is used to generate the system_tests jobs. There will be one job per driver per bitness.
// See https://github.com/ni/nimi-python/wiki/nimi-bot-separate-server-and-agents (this location will change
// once the documentation is finalized)

// Driver list
DRIVERS = [ "nidcpower", "nidigital", "nidmm", "nifgen", "niscope", "niswitch", "nise", "nimodinst" ]
// Platform list - also used as node label
PLATFORMS = [ "win32", "win64" ]

ROOT_FOLDER = "nimi-bot"
credentials_to_use = 'c07926b1-d626-4476-892a-e21bb6d28733'  // nimi-bot username/Personal Access Token

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
                orgWhitelist('ni')
                cron('H/5 * * * *')
                extensions {
                    commitStatus {
                        context("system-tests/${platform}/${driver}")
                        triggeredStatus("triggered...")
                        startedStatus("running...")
                        addTestResults(true)
                        completedStatus('SUCCESS', "")
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
echo Useful environment variables
echo ghprbActualCommit =            %ghprbActualCommit%
echo ghprbActualCommitAuthor =      %ghprbActualCommitAuthor%
echo ghprbActualCommitAuthorEmail = %ghprbActualCommitAuthorEmail%
echo ghprbPullDescription =         %ghprbPullDescription%
echo ghprbPullId =                  %ghprbPullId%
echo ghprbPullLink =                %ghprbPullLink%
echo ghprbPullTitle =               %ghprbPullTitle%
echo ghprbSourceBranch =            %ghprbSourceBranch%
echo ghprbTargetBranch =            %ghprbTargetBranch%
echo ghprbCommentBody =             %ghprbCommentBody%
echo sha1 =                         %sha1%
echo .
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


