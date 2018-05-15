#!/usr/bin/env bash

cat <<'EOF'
<html>
  <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/atom-one-dark.min.css">
    <script>
      const yaml = `
EOF

cat -

cat <<'EOF'

`
    </script>
  </head> 
  <body class="hljs" style="font-size: 1.1rem; margin: 0;">
    <pre id="yaml"></pre>
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

      document.getElementById("yaml").innerHTML = html
    </script>
  </body>
</html>
EOF