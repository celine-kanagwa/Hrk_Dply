mkdir -p ~/.streamlit/

<<<<<<< HEAD
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
=======
echo "
[server]
port = $PORT
enableCORS = false
headless = true
~/.streamlit/config.toml
>>>>>>> 014d9ed23e3333b5f0ba96e775a4456252680e4e
