pipeline {
    agent any
    stages {
        stage('Preparing e-mail') {
            steps {
                emailext attachLog: true, body: 'New Push was detected', compressLog: true, subject: 'Attention!', to: 'agorbach@gmail.com'                
            }
        }
        // stage('Sending e-mail') {
        //     steps {
        //         mail bcc: '', body: 'Your repository was changed', cc: 'alexpitronot@gmail.com', from: '', replyTo: '', subject: 'Attention!!', to: 'agorbach@gmail.com'
        //     }
        // }
        
        stage('Printing output') {
            steps {
                echo 'Now all good 09-01-23'
            }
        }
    }
}


