#!/bin/bash


update_pypi() {
	local username=$(op items get hwgpo3mrfdnvxothu7z6cc3pau --format json --field=username | jq -r '.value')
	local password=$(op items get hwgpo3mrfdnvxothu7z6cc3pau --format json --field=password | jq -r '.value')

	python setup.py bdist_wheel
	twine upload -u "${username}" -p "${password}" --verbose --skip-existing dist/*
}

update_pypi