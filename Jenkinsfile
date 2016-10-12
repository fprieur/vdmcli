node('lab'){
    stage 'modifications dépot git'
    git branch: 'dev', credentialsId: '246beee7-cdff-4ec1-a3b9-2b5d87709585', url: 'git@bitbucket.org:villemontreal/vdmcli.git'
    
    stage 'merge dev -> master'
    sh 'git checkout master'
}
