SKEM_REPO="https://github.com/TeamDaisyX/DaisyX-Extra.git"
FOLDER="./ExtraPlugins"
reqirements_file="./ExtraPlugins/Extrarequirements.txt"


git_clone () {
  git clone "$SKEM_REPO" "$FOLDER"
}

req_installer () {
    pip3 install --no-cache-dir -r "$reqirements_file"
}

fetch_plugins () {
  git_clone
  req_installer
}

fetch_plugins