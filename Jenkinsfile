
stage('Check Download Links') {
    node {
        sh """
            ./bin/check_download_urls.sh
        """
    }
}

stage('Build Docker EXE Creator') {
    node {
        deleteDir()

        checkout scm

        dockerBuild file: './jenkins/Dockerfile',
            tags: ['bmst/pyinstaller-windows-germaniumget-py27']
    }
}

stage('Build EXE File') {
    node {
        dockerRun image: 'bmst/pyinstaller-windows-germaniumget-py27',
            remove: true,
            env: [
                'PYPI_URL=http://nexus:8081/repository/pypi-local/pypi',
                'PYPI_INDEX_URL=http://nexus:8081/repository/pypi-local/simple'
            ],
            links: [
                'nexus:nexus'
            ],
            volumes: [
                // Sad panda, I need to specify the absolute path on the docker host
                // while running in a container.
                "/opt/jenkins_home/jobs/germanium-get/workspace:/src:rw"
            ]

        archiveArtifacts artifacts: 'dist/windows/germanium-get.exe', fingerprint: true
    }
}

