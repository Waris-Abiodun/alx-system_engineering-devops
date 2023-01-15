#!/usr/bin/pup
# Install a package using puppet: specific version of flask (2.1.0)

package{'flask':
  provider => 'pip3',
  ensure   => '2.1.0',
}
