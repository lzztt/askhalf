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
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
  <title>Longzhang Tian's resume</title>
  <script>
    const yaml = `''' + yaml + r'''`
  </script>
</head>

<body>
  <div class="container my-3" style="font-family: Courier New, Courier, monospace;">
    <div id="yaml"></div>
    <footer class="text-secondary border-top mt-4 py-2" style="font-size: 0.9rem">
      This site is open source.
      <a href="''' + repo_link + r'''">Improve this page</a>.
    </footer>
  </div>

  <script>
    const re = /^( *)(- )?([\w ]*\w:)?(.*)$/
    const html = yaml.split('\n').map(line => {
        groups = re.exec(line)
        if (!groups[1]) {
            groups[1] = ''
        } else {
            groups[1] = '&nbsp;'.repeat(groups[1].length);
        }
        groups[2] = groups[2] ? `<span class="text-primary">${groups[2]}</span>` : ''
        groups[3] = groups[3] ? `<span class="text-success">${groups[3]}</span>` : ''
        groups[4] = groups[4] ? `<span class="text-dark">${groups[4]}</span>` : ''
        return groups[1] + groups[2] + groups[3] + groups[4] + '<br>'
    }).join('')

    document.getElementById('yaml').innerHTML = html
  </script>
</body>

</html>'''

def main():
    args = get_args()
    yaml_file = args.yaml
    html_file = args.html
    yaml = read_yaml(yaml_file)
    html = create_html(yaml, get_repo_link())
    write_html(html_file, html)

if __name__ == '__main__':
    main()