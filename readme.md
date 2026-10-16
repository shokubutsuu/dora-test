# Testing dora v1.0.1

## env
`uv venv .venv-dora1 && uv pip install --python .venv-dora1/bin/python "dora-rs==1.0.1" pyarrow`

## try this
`source .venv-dora1/bin/activate`
`~/.dora/bin/dora build dora-test.yml`
`~/.dora/bin/dora run dora-test.yml`