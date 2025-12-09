# Creating a New Module

This guide explains how to add a new learning module to the compass-projects repository.

## Module Directory Structure

Each module should follow this structure:

```
module-XX-technology-name/
├── .devcontainer/
│   └── devcontainer.json
├── README.md
├── [starter files]
├── data/
├── exercises/
└── assignments/
```

## Steps to Create a New Module

### 1. Create the Module Directory

```bash
mkdir -p module-XX-technology-name/.devcontainer
```

Replace `XX` with the module number (e.g., 03, 04) and `technology-name` with the main technology used.

### 2. Create the Dev Container Configuration

Create `.devcontainer/devcontainer.json` with the following structure:

```json
{
  "name": "Module Name",
  "image": "appropriate-base-image",
  "customizations": {
    "vscode": {
      "extensions": [
        "relevant-extension-1",
        "relevant-extension-2"
      ],
      "settings": {
        "setting.key": "value"
      }
    }
  },
  "forwardPorts": [port-numbers],
  "postCreateCommand": "command to install dependencies"
}
```

### 3. Common Base Images

- **Python**: `mcr.microsoft.com/devcontainers/python:3.11`
- **R**: `rocker/shiny-verse:latest` or `rocker/tidyverse:latest`
- **Node.js**: `mcr.microsoft.com/devcontainers/javascript-node:18`
- **Julia**: `julia:latest`
- **Java**: `mcr.microsoft.com/devcontainers/java:11`

### 4. Create the Module README

Include:
- Learning objectives
- Prerequisites
- Getting started instructions
- Contents description
- How to run the code
- Useful resources

### 5. Add Starter Files

Create appropriate starter files for your module:
- Main application/script file
- Configuration files
- Sample data (small files only)
- Exercise templates

### 6. Update Main README

Add your module to the list in the main `README.md` file.

## Best Practices

1. **Keep containers lightweight**: Only install necessary dependencies
2. **Use official images**: Prefer official Microsoft or project-maintained images
3. **Document everything**: Clear instructions help students succeed
4. **Include examples**: Provide working starter code
5. **Forward necessary ports**: Make sure students can access their apps
6. **Test the container**: Build and test before committing

## Example Modules

Refer to existing modules for examples:
- `module-01-r-shiny`: R and Shiny setup
- `module-02-python-reflex`: Python and Reflex setup

## Troubleshooting

### Container won't build
- Check that the base image exists and is accessible
- Verify JSON syntax in `devcontainer.json`
- Review the postCreateCommand for errors

### Extensions not loading
- Ensure extension IDs are correct
- Check that extensions are compatible with the container OS

### Ports not accessible
- Verify ports are listed in `forwardPorts`
- Ensure the application is binding to `0.0.0.0`, not `localhost`
