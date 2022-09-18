# wfrp-foundry-utils
Utils for Foundry (WFRP module mainly)

Collection of utils for Foundry.

Translates
- careers
- skills
- talents
- careers rolltable (do it also in existing worlds for **tables.db** file)
- bestiary

You may use `translate_all` script to translate everything (in module's directory only). Put relevant files into `origs`
subdirectory and run script with module's path as parameter. Script depends on `python3` existence.

As for now only Polish language is supported. Multi-language support will eventually be implemented.
# Important note

I will not add `*_desc` files as it probably violates license. You have to prepare these files by yourself an put it
into `lang/pl/` directory. Their format is as follows:
`original name=description`, one item per line (like ordinary INI file).

For example:

`Athletics=<p>Description</p>`
