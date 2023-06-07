// エラーメッセージ用配列を初期化(配列への追加は.push())
let mess = [];

// 関数一本化(分類、入力値、パターン)
const checkUserInput = (cat, val, pat) => {
    if (!val) mess.push(`${cat}が入力されていません。`);
    else {
        val.match(pat) ? console.log(`${cat}：${val}：正しい入力形式`) : mess.push(`${cat}：入力形式が違います。`);
    }
}
// on　blur

// ボタンクリック時に実行する関数
const clickValidateButton = () => {
    // ボタンクリックごとにエラーメッセージを初期化
    mess = [];

    // テキストボックス入力値をそれぞれ変数に代入

    const UserID = document.getElementById('UserID').value;
    const Password = document.getElementById('Password').value;


    // 入力パターンをそれぞれ変数に代入
    const passwordPattern = /^[\u30a0-\u30ff\u3040-\u309f\u3005-\u3006\u30e0-\u9fcf 　]{1,20}$/;
    const idPattern = /^[a-z0-9]{1,8}$/;

    // 配列に[種別, 値, パターン]をまとめて一本化関数に渡す
    let arr = [
        ['ユーザーID', UserID, idPattern],
        ['パスワード', Password, passwordPattern],
    ];
    arr.forEach(e => checkUserInput(e[0], e[1], e[2]));

    // エラーがなければ確認ボタンをdisableにして「確認完了」メッセージ
    if (mess.length == 0) {
        btn.disabled = true;
        viewOk[0].textContent = '確認完了';
    }
    // エラーが1つでもあれば文字列に結合して1つのアラートで出力
    else {
        alert(mess.join('\n'));
    }
}

// 「確認」ボタンをクリックしたら入力検証を実施
const btn = document.getElementById('validateButton');
const viewOk = document.getElementsByClassName('viewOK');

btn.addEventListener('onclick', () => {
    clickValidateButton();
})
