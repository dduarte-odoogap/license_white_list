# License Module White List

## Introduction

This module creates a whitelist and doesn't allow UI users to install modules without updating that list.
This avoids installing modules that the customer hasn't purchased.

## Usage

When you place this module on the addons path it will *auto-install*
When it installs it will preload the system paramenter 'base.module_lock_list' with a comma separated list of the installed apps (only app modules).

If you need to install more modules just use the command line or first update this list 