const publicKeyEndpoint = 'http://localhost:5000/api/public_key/'
const privateKeyEndpoint = 'http://localhost:5000/api/private_key/'
const encryptEndpoint = 'http://localhost:5000/api/encrypt/'
const decryptEndpoint = 'http://localhost:5000/api/decrypt/'

function getPublicKey() {
  console.log('pressed')
  fetch(publicKeyEndpoint)
    .then((response) => response.text())
    .then((publicKey) => {
      document.getElementById('publicKeyInput').value = publicKey
    })
}

function getPrivateKey() {
  const password = document.getElementById('passwordInput').value
  fetch(`${privateKeyEndpoint}?password=${password}`)
    .then((response) => {
      if (response.status === 401) {
        alert('Invalid password')
        return
      }
      return response.text()
    })
    .then((privateKey) => {
      document.getElementById('privateKeyInput').value = privateKey
    })
}

function getEncryptedMessage() {
  const message = document.getElementById('messageInput').value
  fetch(`${encryptEndpoint}?message=${message}`)
    .then((response) => response.text())
    .then((encrypted) => {
      document.getElementById('encryptedMessageInput').value = encrypted
    })
}

function getDecryptedMessage() {
  const encrypted = document.getElementById('encryptedInput').value
  fetch(`${decryptEndpoint}?encrypted_message=${encrypted}`)
    .then((response) => response.text())
    .then((decrypted) => {
      document.getElementById('decryptedMessageInput').value = decrypted
    })
}
