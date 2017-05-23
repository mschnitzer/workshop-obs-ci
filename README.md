# Exercises:

The exercises are built on top of each other which means you need to e.g. finish exercise one before you can start working on exercise two.
If you stuck with one exercise you can look at the answer in the according branch (exercise-#number).

1. Create a GitHub repository with a simple script in it which prints "Hello World" to the console

2. Create a package in your build.opensuse.org home project

3. The package should contain a spec file which installs your "Hello World" script to /bin
Hints: 
* https://en.opensuse.org/openSUSE:Build_Service_Tutorial

4. The package should contain a _service file which fetches the sources from the GitHub repository you created in the previous step
Hints:
* https://en.opensuse.org/openSUSE:Build_Service_Concept_SourceService

5. Connect GitHub with OBS in order to let GitHub trigger a build if a new commit has been pushed to master
Hints:
* You can create a security token with `osc token`
* You can add a GitHub webhook in your repository via Settings -> Webhooks

6. Create a new appliance in your build.opensuse.org home project by copy over the config.xml and config.sh files from the exercise-6 branch.

7. Add your "Hello World" package to the appliance

8. Add the apache2 package and make sure that apache gets automatically started
Hints:
* You can enable services in the config.sh script
* You can start the apache2 webserver via ``systemctl enable apache2``

9. Add the postgresql94-server and pgadmin3 package to your appliance and make sure that the postgressql server gets started automatically
* You can enable services in the config.sh script
* you can start the postgresql-server via ``systemctl enable postgresql``

10. Add a simple ``Hello World`` html file to your apache2 webserver
Hints:
* You should add the files to the ``/root`` directory
* The root directory needs to be a tar.gz file (``tar -zcvf tar-archive-name.tar.gz source-folder-name``)
* The html files need to go into ``/srv/www/htdocs``

11. Add a postgressql database dump to the `/tmp` directory
Hints:
* You should add the files to the ``/root`` directory
* The root directory needs to be a tar.gz file (``tar -zcvf tar-archive-name.tar.gz source-folder-name``)
