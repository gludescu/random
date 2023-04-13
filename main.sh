#!/bin/bash

# Function to display the menu
function show_menu {
    echo "Select a Python script to run:"
    local i=1
    for script in ./*.py; do
        echo "${i} - $(basename ${script})"
        scripts_list[${i}]="${script}"
        ((i++))
    done
    echo "0 - Exit"
}

# Main loop
while true; do
    show_menu

    read -p "Enter the number of the script you want to run: " choice

    if [[ ${choice} == 0 ]]; then
        echo "Exiting..."
        break
    elif [[ -n "${scripts_list[${choice}]}" ]]; then
        echo "Running ${scripts_list[${choice}]}"
        python3 "${scripts_list[${choice}]}"
    else
        echo "Invalid choice. Please try again."
    fi

    echo ""
done
