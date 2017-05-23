# Exercises: Appliance

1. Create an openSUSE Leap 42.3 image in your build.opensuse.org home project
2. Add your "Hello World" package to the appliance
3. Add the apache2 package and make sure that apache gets automatically started
4. Add the postgressql and pgadmin3 package to your appliance and make sure that the postgressql server gets started automatically
5. Add files to your appliance
5.1. Add a simple `Hello World` index.html file
5.2. Add a postgressql database dump to the `/tmp` directory

Hints:
* You can start apache with `systemctl ...`
* The pgadmin package lives in the ... project
* You can use the `/root` directory to add files to your appliance
