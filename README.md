# muse2-eeg-dashboard
Dashboard to compare sessions recorded with muselsl, using various neurofeedback metrics

## Run & Deploy
You can run a local server to compare your private files.
```
npm run build
npm run deploy
```

Alternatively, the same project has been deployed [here](https://writer-in-fancy-pants.github.io/muse2-eeg-dashboard) 
The website is serverless, running only in the browser. No files will leave your device.

## Converting other csv recordings
`python convert_to_muselsl.py -i <directory_of_csv_files/path_to_csv_file`

By default, the output will be saved in `./converted` which can be changed using
```
python convert_to_muselsl.py -i <directory_of_csv_files/path_to_csv_file> -o <output_directory>
```
