	#!/bin/bash
    
    echo "Did the program run without errors? (Y/N)"

	read solution

	if [[ $solution == "y" || $solution == "Y" ]]; then
		rm -rf ../JPEGImagesOld
	fi