# Johnny Decimal File System Generator

A filesystem generator based on the [Johnny Decimal](https://johnnydecimal.com/) format 

## How to Use  

- Run `main.py` as a shell script ```sh ./main.py``` or with Python ```sh python main.py```
- Configuration and usage can be obtained by running with `-h`

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

## License 

Idk man lol
