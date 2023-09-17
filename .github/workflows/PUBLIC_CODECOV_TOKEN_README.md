# WHY DO WE NEED THIS TOKEN WHEN THE ACTION DOCUMENTATION CLAIMS NO TOKEN IS NEEDED FOR PUBLIC REPOSITORIES?
See ISSUE #2013: codecov-action does not reliably upload system-test coverage to codecov
According to community discussion, failed uploads often occur due to "Codecov’s inability to check the validity
of a coverage upload when using tokenless uploads. The underlying issue is rate-limiting from GitHub."

There are 2 possible fixes:
1. Pass the token, when uploading
2. Implement a retry on upload failure (we do this for travis-ci)

# OKAY, BUT WHY AREN'T WE STORING THIS TOKEN IN A SECRET?
According to GitHub: "With the exception of GITHUB_TOKEN, secrets are not passed to the runner when a workflow is triggered from a forked repository."
We require contributors to fork this repository, so that rules out secrets.

# WHAT ARE THE SECURITY RAMIFICATIONS OF MAKING THIS TOKEN PUBLICLY VISIBLE?
From the community discussion:
"The scope of the Codecov token is only to confirm that the coverage uploaded comes from a specific repository,
not to pull down source code or make any code changes."
"A malicious actor would be able to upload incorrect or misleading coverage reports to a specific repository if
they have access to your upload token, but would not be able to pull down source code or make any code changes."