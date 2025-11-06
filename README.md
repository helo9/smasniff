# smasniff

A python module to collect SMA Speedwire data from your local network.

## Usage

<details>
<summary>Using uv</summary>

```bash
uv run --from https://github.com/helo9/smasniff.git spwdump
```

</details>

<details>
<summary>Using pip</summary>

```bash
pip install https://github.com/helo9/smasniff.git
spwdump
```

</details>

## Common Issues

The communication is often blocked by firewalls.
You need to allow udp port 9522, e.g.

<details>
<summary>Fedora</summary>

Check if the port is allowed

```bash
sudo firewall-cmd --query-port=9522/udp
```

Allow temporarily

```bash
sudo firewall-cmd --add-port=9522/udp # until next reboot
```

or permanent

```bash
sudo firewall-cmd --add-port=9522/udp --permanent
sudo firewall-cmd --reload
```

</details>

<details>
<summary>Debian</summary>

```bash
sudo ufw allow 9522/udp
```

</details>

## License

MIT
