#!/bin/bash
#simple git repository update script for the grendel project
#by chris rehm christopherrehm@web.de
#run this before working on anything to insure all repositories are up to date
cd grendelShares
git pull origin master
cd ../grendelSmallPrograms
git pull origin master
cd ../grendelPhysicalOperationProgram
git submodule update --remote
git pull origin master
cd ../grendelAIandDecisionProgram
git submodule update --remote
git pull origin master
cd ..
git pull origin master

# test
