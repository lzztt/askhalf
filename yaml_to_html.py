#!/usr/bin/env python3

import argparse
import subprocess

def get_args():
    parser = argparse.ArgumentParser(description='Generate a HTML page to display a YAML file')
    parser.add_argument('--yaml', help='the input YAML file', type=str, required=True)
    parser.add_argument('--html', help='the output HTML file', type=str, required=True)
    return parser.parse_args()

def read_yaml(yaml_filename):
    with open(yaml_filename) as f:
        return f.read()

def write_html(html_filename, html):
    with open(html_filename, 'w') as f:
        f.write(html)

def get_repo_link():
    cmd = subprocess.run(['git', 'remote', 'get-url', 'origin'], stdout=subprocess.PIPE)
    return cmd.stdout.decode('utf-8').strip()[:-len('.git')]

def create_html(yaml, repo_link):
    return r'''<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
  <title>ASK HALF</title>
  <script>
    const yaml = `''' + yaml + r'''`
  </script>
  <style>
    body {
      font-family: "Courier New", Courier, monospace;
    }
    .container span {
      white-space: pre-wrap;
    }
  </style>
</head>

<body>
  <div class="container">
    <header class="my-3" style="font-size: 1.2rem">
      <span class="bg-success text-white p-1 pl-2 border border-success rounded-left">Ask</span><span class="bg-white text-success p-1 pr-2 border border-success rounded-right">Half</span>
      <span class="p-1 text-capitalize d-block d-sm-inline">Be your best self. Better journey together.</span>
    </header>
    <div id="yaml"></div>
    <footer class="text-black-50 border-top mt-4 py-2" style="font-size: 0.9rem">
      Created by <a target="_blank" href="https://www.linkedin.com/in/lzt/">Longzhang Tian</a>.<br>
      This work is licensed under a <a target="_blank" rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
    </footer>
  </div>

  <script>
    const re = /( *)(- )?([\w ]*\w: *)?(\[)?([^#\[\]]*)?(\])?(#.*)?/
    const html = yaml.split('\n').map(line => {
        groups = re.exec(line)
        groups[1] = groups[1] ? `<span>${groups[1]}</span>` : ''
        groups[2] = groups[2] ? `<span class="text-primary">${groups[2]}</span>` : ''
        groups[3] = groups[3] ? `<span class="text-success">${groups[3]}</span>` : ''
        groups[4] = groups[4] ? `<span class="text-black-50">${groups[4]}</span>` : ''
        groups[5] = groups[5] ? `<span class="text-dark">${groups[5]}</span>` : ''
        groups[6] = groups[6] ? `<span class="text-black-50">${groups[6]}</span>` : ''
        groups[7] = groups[7] ? `<span class="text-black-50">${groups[7]}</span>` : ''
        return groups.slice(1, 8).join('')
    }).join('<br>')

    document.getElementById('yaml').innerHTML = html
  </script>
</body>

</html>'''

def main():
    args = get_args()
    yaml_file = args.yaml
    html_file = args.html
    yaml = read_yaml(yaml_file).strip()
    html = create_html(yaml, get_repo_link())
    write_html(html_file, html)

if __name__ == '__main__':
    main()
