module.exports = {
    browser: ['safari'],
    injectChanges: false,
    ghostMode: false,
    minify: false,
    notify: false,
    port: 3000,
    reloadOnRestart: true,
    server: {
        baseDir: 'site',
        index: 'index.html',
        serveStaticOptions: {
            extensions: ['html'],
        },
    },
    watch: true,
}
