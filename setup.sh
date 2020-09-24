mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS=false\n\
\n\
[deprecation]
showPyplotGlobalUse = False
" > ~/.streamlit/config.toml