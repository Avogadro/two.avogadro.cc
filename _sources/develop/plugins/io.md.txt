(develop-plugins-io)=

#### The input JSON

| Key                               | JSON data type        | Value                                                     | Feature types                         | Applicable    |
| ---                               | ---                   | ---                                                       | ---                                   | ---           |
| `config`                          | `object`              | The user's stored configuration of the plugin             | All                                   | `user-config` is specified |
| `cjson`                           | `object`              | The current CJSON file in full                            | All except `file-formats`             | `input-cjson = true` or `input-format = "cjson"` |
| `xyz`, `cml`, `pdb`, `cif`, `sdf`, `mdl`, `mol`, etc. | `string` | The contents of a file in the respective format    | All except `file-formats`             | `input-format = <fmt>` |
| `file`                            | `string`              | A path to a file in the filesystem                        | `file-formats`                        | Always        |
| `options`                         | `object`              | Key/value pairs for each option requested in `user-options` | `menu-commands`, `input-generators` | Always        |
| `points`                          | `array` of `number`   | The coordinates of the requested points                   | `electrostatic-models`                | Called with `--potentials` |
| `selectedAtoms`                   | `array` of `number`   | The indices of the atoms that are currently selected      | `menu-commands`                       | Always        |

#### The output JSON

| Key                               | JSON data type        | Value                                                     | Feature types             | Applicable    |
| ---                               | ---                   | ---                                                       | ---                       | ---           |
| `message`                         | `string`              | A message to display to the user in a pop-up dialog       | All                       | Always        |
| `error`                           | `string`              | Similar, but displays an error, and the plugin is stopped | All                       | Always        |
| `config`                          | `object`              | The user's configuration of the plugin as it should be saved | All                    | `user-config` is specified |
| `cjson`                           | `object`              | A CJSON file to be loaded                                 | All?                      | `output-format = "cjson"` |
| `xyz`, `cml`, `pdb`, `cif`, `sdf`, `mdl`, `mol`, etc. | `string` | The contents of a file in the respective format    | All?                      | `output-format = <fmt>` |
| `charges`                         | `array` of `number`   | The partial charges on each atom                          | `electrostatic-models`    | Called with `--charges` |
| `potentials`                      | `array` of `number`   | The electrostatic potential at each requested point       | `electrostatic-models`    | Called with `--potentials` |
| `bond`                            | `bool`                | Whether Avogadro should run automatic bond perception     | `menu-commands`           | Always        |
| `selectedAtoms`                   | `array` of `number`   | The indices of the atoms that Avogadro should select      | `menu-commands`           | Always        |
| `warnings`                        | `array` of `string`   | Non-fatal warnings to be shown in the generator's dialog  | `input-generators`        | Always        |
| `generatedFiles`                  | `object`              | Details of several files                                  | `input-generators`        | Always        |
| `mainFile`                        | `string`              | The primary input file for a calculation                  | `input-generators`        | Always        |
