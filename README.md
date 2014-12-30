# [ansible-vagrant][]

Tired of the rather limited `vagrant provision` with the [ansible][] provider?
Tired of keeping your `hosts` file up to date? [ansible-vagrant][] to the rescue!

## Usage

    $ pip install ansible-vagrant
    $ cd /path/to/project/with/a/vagrantfile

    $ ansible-vagrant-update-hosts
    $ cat hosts_vagrant
    [vagrant]
    vagrant  ansible_ssh_host=127.0.0.1  ansible_ssh_port=2222  ansible_ssh_use...

    $ ansible-vagrant all -m ping
    # Same as: ansible-vagrant-update-hosts \
    #          && ansible all --inventory=./hosts_vagrant -m ping

    $ ansible-playbook-vagrant playbook.yml
    # Same as: ansible-vagrant-update-hosts \
    #          && ansible-playbook --extra-vars="vagrant_host=true" \
    #                              --inventory=./hosts_vagrant playbook.yml

## Notes

- All `*-vagrant` commands use `ANSIBLE_HOST_KEY_CHECKING=False` to prevent
  errors with `vagrant destroy && vagrant up`
- It's a good idea to put `hosts_vagrant` under `.gitignore`
- `ansible-playbook-vagrant` adds a global variable named `vagrant`
- Use `when: vagrant_host is (not) defined` to run stuff based on the current
  environment

## Shortcuts

* `ansiblev` for `ansible-vagrant`
* `ansible-playbookv` for `ansible-playbook-vagrant`

  [ansible]: https://github.com/ansible/ansible
  [ansible-vagrant]: https://github.com/michaelcontento/ansible-vagrant
