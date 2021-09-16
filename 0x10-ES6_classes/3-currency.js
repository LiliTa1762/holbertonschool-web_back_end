export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(Newcode) {
    this._code = Newcode;
  }

  set name(Newname) {
    this._name = Newname;
  }

  displayFullCurrency() {
    return (`${this._name} (${this._code})`);
  }
}
