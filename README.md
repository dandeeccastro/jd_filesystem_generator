# Johnny Decimal File System Generator

> A filesystem generator based on the [Johnny Decimal](https://johnnydecimal.com/) format 

## Installation 

- Clone this repository and make sure you have ```sh pip``` installed
- `cd` into the repository in order to run the program

## Usage 

- Write a YAML file following proper formatting (as exemplified in the default YAML file)
- Run`main.py` as a shell script ```sh ./main.py``` or with Python ```sh python main.py``` 
  - Specify your custom yaml file with `-f <file>`
  - Specify which directory you wish to build the tree with `-p <path>`
  - Configuration and usage can be obtained by using the `-h` flag

## Roadmap 

- [ ] Implement as a PIP module

- [x] Add command line arguments
	- [x] Choose which yml file to use as configuration
	- [x] Choose which directory to create the filesystem

- [ ] Error handling
	- [ ] For when there is already a filesystem on the chosen path
	- [ ] For when the YAML file is poorly formatted 
	- [ ] For other errors (I haven't tested it thoroughly)

- [ ] New features
	- [ ] Maybe update one filesystem based on another?

## Contributing

While I have no prior experience in contributing to open source projects, I'll do my best to check pull requests and suggested changes to the script, so feel free to send changes and suggestions!
