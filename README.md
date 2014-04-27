# [ansible-vagrant][]

Tired of the rather limited `vagrant provision` with the [ansible][] provider?
Tired of keeping your `hosts` file up to date? [ansible-vagrant][] to the rescue!

## Usage

    $ pip install ansible-vagrant
    $ cd /path/to/project/with/a/vagrantfile

    $ ansible-vagrant-update-hosts
    $ cat hosts
    vagrant  ansible_ssh_host=127.0.0.1  ansible_ssh_port=2222  ansible_ssh_use...

    $ ansible-vagrant all -m ping
    # Same as: ansible-vagrant-update-hosts && ansible all -m ping

    $ ansible-playbook-vagrant playbook.yml
    # Same as: ansible-vagrant-update-hosts && ansible-playbook paybook.yml

## Shortcuts

* `ansiblev` for `ansible-vagrant`
* `ansible-playbookv` for `ansible-playbook-vagrant`

  [ansible]: https://github.com/ansible/ansible
  [ansible-vagrant]: https://github.com/michaelcontento/ansible-vagrant
