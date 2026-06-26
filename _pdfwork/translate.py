#!/usr/bin/env python3
"""Recreate the LEIN Marrakech catalogue with French text, keeping layout/images/colors identical."""
import fitz

SRC = "/root/.claude/uploads/4331ce8a-d1f5-5df0-95fe-c512fb86886c/5c879802-LEIN_MARRAKECH_CATALOGUE_Livret_final.pdf"
OUT = "/home/user/test/_pdfwork/LEIN_MARRAKECH_CATALOGUE_FR.pdf"
FD  = "/home/user/test/_pdfwork/fonts/static"

FONTS = {
    "ibR":  f"{FD}/Ibarra-Regular.ttf",
    "ibB":  f"{FD}/Ibarra-Bold.ttf",
    "ibI":  f"{FD}/Ibarra-Italic.ttf",
    "ibBI": f"{FD}/Ibarra-BoldItalic.ttf",
    "jL":   f"{FD}/Jost-Light.ttf",
    "jSB":  f"{FD}/Jost-SemiBold.ttf",
    "osR":  f"{FD}/OpenSans-Regular.ttf",
}
_fontobj = {k: fitz.Font(fontfile=v) for k, v in FONTS.items()}

def rgb(i):
    return ((i >> 16 & 255) / 255, (i >> 8 & 255) / 255, (i & 255) / 255)

CX = 209.6  # page horizontal centre

# --- translation blocks -------------------------------------------------------
# each draw: lines, font, size, color, align('c'/'l'), ax(anchor x), y0(first baseline),
#            step(line spacing), box_w(width for auto-shrink), tracking
PAGES = {
0: dict(redact=[(83,539,337,562)], draws=[
    dict(lines=["UN VOYAGE INTÉRIEUR. . ."], font="jSB", size=20.2, color=0x000000,
         align="c", ax=CX, y0=557.5, step=0, box_w=300, tracking=1.2)]),

1: dict(redact=[(62,210,272,298),(62,330,272,351)], draws=[
    dict(lines=["Il existe en vous un lieu","Qui connaît le calme.",
                "Un lieu où le bruit s'efface,","Où le corps s'apaise,",
                "Où vous revenez à vous-même."],
         font="ibI", size=12.7, color=0x231f20, align="l", ax=62.8, y0=223.7, step=17.42, box_w=160),
    dict(lines=["Votre voyage intérieur commence ici."],
         font="ibBI", size=14.8, color=0x231f20, align="l", ax=62.8, y0=345.3, step=0, box_w=215)]),

2: dict(redact=[(41,114,194,146),(41,201,194,224),(41,233,194,277),
                (41,286,194,351),(41,360,194,383),(118,402,194,414)], draws=[
    dict(lines=["À PROPOS"], font="jL", size=28.9, color=0x5a3022,
         align="l", ax=41.9, y0=137.2, step=0, box_w=200, tracking=1.0),
    dict(lines=["LEIN Marrakech est une maison de rituels bien-être",
                "née au cœur de Marrakech."],
         font="ibB", size=7.7, color=0x231f20, align="l", ax=41.9, y0=209.8, step=10.5, box_w=151),
    dict(lines=["Chaque pièce est façonnée à la main par des maîtres",
                "potiers, selon des techniques ancestrales transmises",
                "de génération en génération — donnant à chaque",
                "objet son propre caractère, sa propre histoire."],
         font="ibB", size=7.7, color=0x231f20, align="l", ax=41.9, y0=241.4, step=10.55, box_w=151),
    dict(lines=["Nos formules sont élaborées avec des ingrédients",
                "soigneusement choisis et nourrissants pour la peau :",
                "beurre de karité, beurre de cacao et huiles",
                "essentielles pures. Conçues non seulement pour",
                "prendre soin de la peau, mais pour transformer un",
                "instant ordinaire en un souvenir précieux."],
         font="ibB", size=7.7, color=0x231f20, align="l", ax=41.9, y0=294.3, step=10.55, box_w=151),
    dict(lines=["Voilà ce qu'est LEIN — la rencontre de l'artisanat",
                "marocain et de l'art de prendre soin de soi."],
         font="ibB", size=7.7, color=0x231f20, align="l", ax=41.9, y0=368.2, step=10.6, box_w=151),
    dict(lines=["Votre voyage intérieur."],
         font="ibB", size=7.7, color=0x231f20, align="l", ax=119.2, y0=410.5, step=0, box_w=75)]),

3: dict(redact=[(107,283,312,314),(116,310,304,341),(48,355,371,378)], draws=[
    dict(lines=["LA COLLECTION"], font="jL", size=28.9, color=0x5a3022,
         align="c", ax=CX, y0=305.8, step=0, box_w=320, tracking=1.0),
    dict(lines=["ORIGINALE"], font="jL", size=28.9, color=0x5a3022,
         align="c", ax=CX, y0=332.8, step=0, box_w=320, tracking=1.0),
    dict(lines=["La collection où le rituel Leïn a vu le jour"],
         font="osR", size=14.4, color=0x5a3022, align="c", ax=CX, y0=372.3, step=0, box_w=345)]),

4: dict(redact=[(123,523,297,547)], draws=[
    dict(lines=["Bougie de massage artisanale"],
         font="ibR", size=16.9, color=0x6b6657, align="c", ax=CX, y0=540.5, step=0, box_w=300)]),

5: dict(redact=[(88,71,332,109),(23,131,396,190),(23,207,396,266),(23,283,396,323)], draws=[
    dict(lines=["QUAND L'ATLAS RENCONTRE"], font="jL", size=18.3, color=0x5a3022,
         align="c", ax=CX, y0=86.2, step=0, box_w=320, tracking=0.8),
    dict(lines=["VOTRE PEAU"], font="jL", size=18.3, color=0x5a3022,
         align="c", ax=CX, y0=103.1, step=0, box_w=320, tracking=0.8),
    dict(lines=["Des montagnes d'un blanc neigeux. Les vents de l'Atlas",
                "portant le parfum du cèdre et des herbes sauvages. Un",
                "silence qui vous enveloppe comme la soie."],
         font="osR", size=13.7, color=0x5a3022, align="c", ax=CX, y0=147.1, step=18.9, box_w=375),
    dict(lines=["Voile d'Atlas se fond en une huile corporelle chaude et",
                "ultra-nourrissante, infusée de vanille de Madagascar,",
                "d'ambre, de fève tonka et de musc doux."],
         font="osR", size=13.7, color=0x5a3022, align="c", ax=CX, y0=223.1, step=18.9, box_w=375),
    dict(lines=["Allumez-la. Laissez-la respirer. Versez l'huile tiède",
                "délicatement sur la peau — et abandonnez-vous au rituel."],
         font="osR", size=13.7, color=0x5a3022, align="c", ax=CX, y0=299.2, step=18.9, box_w=375)]),

6: dict(redact=[(123,524,297,547)], draws=[
    dict(lines=["Bougie de massage artisanale"],
         font="ibR", size=16.9, color=0x6b6657, align="c", ax=CX, y0=541.1, step=0, box_w=300)]),

7: dict(redact=[(34,184,385,225),(29,264,390,305),(106,352,313,373)], draws=[
    dict(lines=["Jardins de riad cachés. Agrumes. Murs de",
                "terracotta chauds sous le soleil de Marrakech."],
         font="osR", size=14.4, color=0x5a3022, align="c", ax=CX, y0=200.2, step=20.1, box_w=360),
    dict(lines=["Jardin Caché se fond en une huile de massage soyeuse",
                "conçue pour nourrir la peau tout en éveillant les sens."],
         font="osR", size=14.4, color=0x5a3022, align="c", ax=CX, y0=280.5, step=20.1, box_w=362),
    dict(lines=["Mandarine • Basilic • Herbes fraîches"],
         font="osR", size=14.4, color=0x5a3022, align="c", ax=CX, y0=368.4, step=0, box_w=320)]),

8: dict(redact=[(37,482,383,503),(121,106,298,129),(26,512,393,573)], draws=[
    dict(lines=["Guimauve • Vanille crémeuse • Ambre • Musc doux"],
         font="osR", size=14.4, color=0x5a3022, align="c", ax=CX, y0=498.0, step=0, box_w=360),
    dict(lines=["Chaude. Solaire. Addictive."],
         font="ibR", size=16.9, color=0x5a3022, align="c", ax=CX, y0=123.6, step=0, box_w=300),
    dict(lines=["Conçue pour hydrater et sublimer le corps d'un éclat",
                "radieux tout en laissant la peau délicatement parfumée",
                "longtemps après l'application."],
         font="osR", size=14.4, color=0x5a3022, align="c", ax=CX, y0=528.6, step=20.05, box_w=370)]),

9: dict(redact=[(95,89,324,111),(135,346,297,368)], draws=[
    dict(lines=["Huile sèche scintillante et légère"],
         font="ibR", size=16.9, color=0x6b6657, align="c", ax=CX, y0=105.3, step=0, box_w=300),
    dict(lines=["Brume sérum hydratante"],
         font="ibR", size=16.9, color=0x6b6657, align="c", ax=CX, y0=362.7, step=0, box_w=300)]),

10: dict(redact=[(125,103,295,135),(239,446,378,467),(95,227,324,246),
                 (95,267,324,287),(109,308,310,326),(121,348,298,367),(96,388,323,407)], draws=[
    dict(lines=["LE RITUEL"], font="jL", size=28.9, color=0x5a3022,
         align="c", ax=CX, y0=126.2, step=0, box_w=300, tracking=1.0),
    dict(lines=["I. Allumez la bougie. Laissez-la respirer."],
         font="ibI", size=12.7, color=0x231f20, align="c", ax=CX, y0=240.9, step=0, box_w=340),
    dict(lines=["II. Attendez que le mélange se fonde en huile tiède."],
         font="ibI", size=12.7, color=0x231f20, align="c", ax=CX, y0=281.1, step=0, box_w=360),
    dict(lines=["III. Versez délicatement sur la peau. Respirez."],
         font="ibI", size=12.7, color=0x231f20, align="c", ax=CX, y0=321.2, step=0, box_w=340),
    dict(lines=["IV. Fermez les yeux. Vous êtes ici."],
         font="ibI", size=12.7, color=0x231f20, align="c", ax=CX, y0=361.4, step=0, box_w=340),
    dict(lines=["Chaleur. Éclat. Brume. Le rituel est accompli."],
         font="ibI", size=12.7, color=0x231f20, align="c", ax=CX, y0=401.5, step=0, box_w=340),
    dict(lines=["Votre voyage intérieur."],
         font="ibBI", size=14.8, color=0x231f20, align="c", ax=308.5, y0=461.3, step=0, box_w=140)]),

11: dict(redact=[(82,266,337,290)], draws=[
    dict(lines=["DÉCOUVREZ LE RITUEL"], font="jL", size=22.6, color=0x46251a,
         align="c", ax=CX, y0=283.9, step=0, box_w=300, tracking=0.8)]),
}

def draw_line(page, text, font, size, color, baseline_y, align, ax, tracking):
    fo = _fontobj[font]
    fp = FONTS[font]
    col = rgb(color)
    if tracking and tracking > 0:
        widths = [fo.text_length(ch, size) for ch in text]
        total = sum(widths) + tracking * (len(text) - 1)
        x = ax - total / 2 if align == "c" else ax
        for ch, w in zip(text, widths):
            page.insert_text((x, baseline_y), ch, fontname=font, fontfile=fp,
                             fontsize=size, color=col)
            x += w + tracking
    else:
        w = fo.text_length(text, size)
        x = ax - w / 2 if align == "c" else ax
        page.insert_text((x, baseline_y), text, fontname=font, fontfile=fp,
                         fontsize=size, color=col)

def fit_size(lines, font, size, box_w, tracking):
    fo = _fontobj[font]
    def width(t, s):
        w = fo.text_length(t, s)
        if tracking:
            w += tracking * (len(t) - 1)
        return w
    mx = max(width(t, size) for t in lines)
    if mx > box_w:
        size = size * box_w / mx
    return size

def main():
    doc = fitz.open(SRC)
    for pno, cfg in PAGES.items():
        page = doc[pno]
        for r in cfg["redact"]:
            page.add_redact_annot(fitz.Rect(r), fill=False)
        page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE,
                              graphics=fitz.PDF_REDACT_LINE_ART_NONE,
                              text=fitz.PDF_REDACT_TEXT_REMOVE)
        for d in cfg["draws"]:
            trk = d.get("tracking", 0)
            size = fit_size(d["lines"], d["font"], d["size"], d["box_w"], trk)
            for k, line in enumerate(d["lines"]):
                by = d["y0"] + k * d["step"]
                draw_line(page, line, d["font"], size, d["color"], by,
                          d["align"], d["ax"], trk)
    doc.subset_fonts()
    doc.save(OUT, garbage=4, deflate=True)
    print("saved", OUT)

if __name__ == "__main__":
    main()
