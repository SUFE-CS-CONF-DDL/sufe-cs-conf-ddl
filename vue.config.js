module.exports = {
  pages: {
    index: {
      entry: 'src/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'sufe-cs-conf-ddl',
    },
  },
  runtimeCompiler: true,
};

// Annotation
// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true,
//  lintOnSave:false
// })
