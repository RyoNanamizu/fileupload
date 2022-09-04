'use strict'
function str2ab(str) {
  const buf = new ArrayBuffer(str.length)
  const bufView = new Uint8Array(buf)
  for (let i = 0, strLen = str.length; i < strLen; i++) {
    bufView[i] = str.charCodeAt(i)
  }
  return buf
}

const encrypt = async (file, publicKey) => {
  const publicKeyBinary = str2ab(atob(publicKey))
  const publicKeyImported = await window.crypto.subtle.importKey(
    'pkcs8',
    publicKeyBinary,
    {
      name: 'RSA-PSS',
      hash: 'SHA-256',
    },
    false,
    ['encrypt']
  )

  const aesKey = await window.crypto.subtle.generateKey(
    {
      name: 'AES-GCM',
      length: 256,
    },
    true,
    ['encrypt', 'decrypt']
  )
  const encryptedAesKey = await window.crypto.subtle.encrypt(
    {
      name: 'RSA-OAEP',
    },
    publicKeyImported,
    await window.crypto.subtle.exportKey('raw', aesKey)
  )
  const iv = new Uint8Array(96 / 8)
  window.crypto.getRandomValues(iv)
  const encryptFile = await window.crypto.subtle.encrypt(
    {
      name: 'AES-GCM',
      iv,
    },
    aesKey,
    await file.arrayBuffer()
  )
  return {
    key: new Blob([encryptedAesKey]),
    file: new Blob([encryptFile]),
  }
}
