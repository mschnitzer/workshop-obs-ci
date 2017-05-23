# Exercises: Package

1. Create a GitHub repository with a simple script which prints "Hello World" to the console
2. Create a package in your build.opensuse.org home project
3. The package should contain a spec file which installs your "Hello World" script to /bin
4. The package should contain a _service file which fetches the sources from the GitHub repository you created in the previous step
5. Connect GitHub with OBS in order to let GitHub trigger a build if a new commit has been pushed to master

Hints:
* https://en.opensuse.org/openSUSE:Build_Service_Concept_SourceService
* You can create a security token with `osc token ...`
