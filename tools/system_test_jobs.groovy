// Driver list
// DRIVERS = [ "nidcpower", "nidigital", "nidmm", "nifgen", "niscope", "niswitch", "nise", "nimodinst" ]
DRIVERS = [ "nidcpower", "nidigital" ]
// Platform list - also used as node label
PLATFORMS = [ "win32", "win64" ]

ROOT_FOLDER = "nimi-bot"

// This function generates a job for the given driver and platform
// returns generatd job name
def genJob(driver, platform) {
    jobName = "${ROOT_FOLDER}/${platform}/${driver}"
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
                    credentials('863d43e0-e019-4254-b55a-8ea9a7edf9a1')
                }
            }
        }

        triggers {
            scm('H/3 * * * *')
        }

        // Once we suppot Linux, we will need to generate the steps differently
        steps {
            gitStatusWrapperBuilder {
                buildSteps {
                    batchFile {
                        command("""@echo off
echo Running system tests for ${driver} on ${platform}
tools\\system_tests.bat
""")
                    }
                }
                gitHubContext("system_tests/jenkins/${platform}/${driver}")
                description("System test for ${driver} on ${platform}")
                credentialsId('863d43e0-e019-4254-b55a-8ea9a7edf9a1')
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
