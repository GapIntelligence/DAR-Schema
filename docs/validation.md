# Validating DAR Files

The repository includes a JSON Schema (`dar.schema.json`) that defines the
required structure of a DAR file. The `dar_validator.py` utility uses this schema
to ensure your files comply with the specification.

## Installation

The validator relies on the [`jsonschema`](https://pypi.org/project/jsonschema/)
package. Install it with pip:

```bash
pip install jsonschema
```

## Running the Validator

Provide the path to a DAR file and optionally a custom schema path:

```bash
python tools/validators/dar_validator.py example.dar
```

If you want to use a different schema file:

```bash
python tools/validators/dar_validator.py example.dar custom_schema.json
```

The script prints a validation report listing any issues. A successful run will
output:

```
DAR file is valid and conforms to the schema.
```

Use this tool as part of your workflow to verify that generated DAR files follow
the documented format.
