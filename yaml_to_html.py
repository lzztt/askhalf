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
    return r'''<html>
  <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/atom-one-dark.min.css">
    <script>
      const yaml = `''' + yaml + r'''`
    </script>
  </head> 
  <body class="hljs" style="margin: 0; padding: 1rem; font: 1.1rem monospace;">
    <pre id="yaml"></pre>
    <footer>
      This site is open source.
      <a href="''' + repo_link + r'''" class="hljs-link">Improve this page</a>.
    </footer>
    <script>
      const re = /^( *)(- )?([\w ]*\w:)?(.*)$/
      const html = yaml.split('\n').map(line => {
          groups = re.exec(line)
          if (!groups[1]) {
              groups[1] = ''
          }
          groups[2] = groups[2] ? `<span class="hljs-bullet">${groups[2]}</span>` : ''
          groups[3] = groups[3] ? `<span class="hljs-attr">${groups[3]}</span>` : ''
          groups[4] = groups[4] ? `<span class="hljs-string">${groups[4]}</span>` : ''
      
          return groups[1] + groups[2] + groups[3] + groups[4]
      }).join('\n')

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