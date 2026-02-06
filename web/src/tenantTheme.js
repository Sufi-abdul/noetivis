
export const DEFAULT_THEME = {
  brand: "NOETIVIS",
  accent: "#00ffe0",
  bg: "#05070f",
  text: "#e6fff9",
};

export function loadTenantTheme(){
  try{
    const raw = localStorage.getItem("noetivis_theme");
    if(!raw) return DEFAULT_THEME;
    return {...DEFAULT_THEME, ...JSON.parse(raw)};
  }catch{
    return DEFAULT_THEME;
  }
}
