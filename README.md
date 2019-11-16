# elementary-staging-rpms
I use this repository to keep track of files related to packaging / building
stable releases of elementaryOS / Pantheon desktop components and applications
for fedora - where they aren't already available from the official fedora
repositories.

Most components of a Pantheon session and almost all elementary apps are
available from the official fedora repositories. The packages maintained here
have outstanding problems that prevent them from working right on fedora, or
have issues that would prevent a successful package review.

## Known Issues

- The Date & Time plug doesn't fully work as expected.
- The Locale plug doesn't seem to work at all under fedora - mainly due to
  assuming `apt` to be the package manager on the system.
- The Parental Controls plug might not work as advertised.
- The Power plug needs a patch to not crash, which leads to reduced
  functionality, and it might not work as expected.
- The Security & Privacy plug doesn't work as expected (and it depends on a
  non-standard firewall, `ufw`).
- The User Accounts plug isn't tested enough to enter fedora repositories - I
  don't want this to break users' machines.

## Package Status

The current build status of all non-official fedora packages can be seen at
<https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-staging/monitor/>.

