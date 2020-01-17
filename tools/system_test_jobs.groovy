// This file is used to generate the system_tests jobs. There will be one job per driver per bitness.
// See https://github.com/ni/nimi-python/wiki/nimi-bot-separate-server-and-agents (this location will change
// once the documentation is finalized)

// Driver list
DRIVERS = [ "nidcpower", "nidigital", "nidmm", "nifgen", "niscope", "niswitch", "nise", "nimodinst" ]
// Platform list - also used as node label
PLATFORMS = [ "win32", "win64" ]

ROOT_FOLDER = "nimi-bot"

// This function generates a job for the given driver and platform
// returns generatd job name
def genJob(driver, platform) {
    jobName = "${ROOT_FOLDER}/${platform}/${driver}"
    println "Processing ${jobName}"
    job("${jobName}") {
        description "Run system tests for ${driver} on ${platform}"

        label(platform)

        scm {
            git {
                branch('generate_jenkins_jobs')
                extensions {
                    wipeWorkspace()
                }
                remote {
                    github('ni/nimi-python')
                    credentials('44e8e6ce-9dc2-486e-bf50-9c015febb7bf')
                }
            }
        }

        triggers {
            scm('H/3 * * * *')
        }

        // Once we add automated system tests on Linux, we will need to generate the steps differently
        steps {
            gitStatusWrapperBuilder {
                buildSteps {
                    batchFile {
                        command("""@echo off
echo Running system tests for ${driver} on ${platform}
tools\\system_tests.bat ${driver}
""")
                    }
                }
                gitHubContext("system_tests/jenkins/${platform}/${driver}")
                description("System tests for ${driver} on ${platform}")
                credentialsId('44e8e6ce-9dc2-486e-bf50-9c015febb7bf')
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

println(jobList.join(','))
