const svg = document.getElementById('viz');
const W = 1100, H = 640; svg.setAttribute('viewBox', `0 0 ${W} ${H}`);

function create(tag, attrs = {}) { const el = document.createElementNS('http://www.w3.org/2000/svg', tag); for (const k in attrs) el.setAttribute(k, attrs[k]); return el; }

// Clear
function clear() { while (svg.firstChild) svg.removeChild(svg.firstChild); }

// Step 1: single silicon atom (Bohr model)
function drawAtom(cx, cy, scale = 1) {
    clear();
    // nucleus (protons + neutrons) stylized
    const nuc = create('g', {});
    const nucleus = create('circle', { cx: cx, cy: cy, r: 18 * scale, class: 'nucleus' });
    const core = create('circle', { cx: cx, cy: cy, r: 10 * scale, class: 'atom-core' });
    nuc.appendChild(nucleus); nuc.appendChild(core);
    svg.appendChild(nuc);

    // Silicon: atomic number 14 -> 14 electrons. Bohr shells (approx): 2,8,4 -> radii
    const shells = [{ r: 40 * scale, count: 2 }, { r: 80 * scale, count: 8 }, { r: 120 * scale, count: 4 }];
    shells.forEach((sh, si) => {
        // orbit path
        const orb = create('circle', { cx: cx, cy: cy, r: sh.r, fill: 'none', stroke: 'rgba(255,255,255,0.04)' });
        svg.appendChild(orb);
        for (let i = 0; i < sh.count; i++) {
            const ang = (i / sh.count) * Math.PI * 2 - Math.PI / 6;
            const ex = cx + Math.cos(ang) * sh.r, ey = cy + Math.sin(ang) * sh.r;
            const e = create('circle', { class: 'electron', cx: ex, cy: ey, r: 6 });
            svg.appendChild(e);
            // small orbit animation
            const g = create('g', {});
        }
    });

    // label
    const label = create('text', { x: cx, y: cy + 170, 'text-anchor': 'middle', 'font-size': 14 }); label.textContent = 'Silicon atom (Bohr model) — Z=14'; svg.appendChild(label);
}

// Step 2: lattice — simplified 2D depiction showing covalent sharing (each Si shares 4 electrons)
function drawLattice() {
    clear();
    // draw a grid of atoms (staggered) and bonds (shared electrons between neighbors)
    const cols = 6, rows = 3; const spacingX = 150, spacingY = 130; const offsetX = 200, offsetY = 140;
    const atoms = [];
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const stagger = (r % 2) * 0.5;
            const x = offsetX + (c + stagger) * spacingX; const y = offsetY + r * spacingY;
            atoms.push({ x, y });
        }
    }
    // draw atoms
    atoms.forEach(a => {
        const g = create('g', {});
        const core = create('circle', { cx: a.x, cy: a.y, r: 12, class: 'atom-core' });
        g.appendChild(core);
        svg.appendChild(g);
    });
    // create covalent bonds: each Si shares electrons with up to 4 neighbors (approx)
    for (let i = 0; i < atoms.length; i++) {
        for (let j = i + 1; j < atoms.length; j++) {
            const a = atoms[i], b = atoms[j]; const dx = a.x - b.x, dy = a.y - b.y; const d = Math.hypot(dx, dy);
            if (d < 140) {
                const line = create('line', { x1: a.x, y1: a.y, x2: b.x, y2: b.y, class: 'bond' });
                svg.appendChild(line);
                // shared electron pair drawn midway
                const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
                const e1 = create('circle', { cx: mx - 8, cy: my - 6, r: 5, class: 'electron' });
                const e2 = create('circle', { cx: mx + 8, cy: my + 6, r: 5, class: 'electron' });
                svg.appendChild(e1); svg.appendChild(e2);
            }
        }
    }
    const label = create('text', { x: W / 2, y: 40, 'text-anchor': 'middle', 'font-size': 16 }); label.textContent = 'Silicon lattice — covalent sharing (each Si forms 4 bonds)'; svg.appendChild(label);
}

// Step 3: N-type doping (donor like Phosphorus with 5 valence electrons) -> extra electron
function drawNdope() {
    clear(); drawLattice();
    // add donor at a chosen atom
    const donorX = 200 + 2 * 150; const donorY = 140 + 1 * 130;
    // highlight donor atom
    const donorCore = create('circle', { cx: donorX, cy: donorY, r: 18, class: 'donorAtom' });
    svg.appendChild(donorCore);
    // extra electron leaving donor into conduction (animated)
    const extra = create('circle', { cx: donorX + 30, cy: donorY - 40, r: 6, fill: 'var(--donor)' });
    svg.appendChild(extra);
    // animate it moving to the right
    extra.animate([{ transform: 'translate(0,0)' }, { transform: 'translate(220px,-60px)' }, { opacity: 0.12 }], { duration: 1600, fill: 'forwards' });
    const label = create('text', { x: W / 2, y: 40, 'text-anchor': 'middle', 'font-size': 16 }); label.textContent = 'N-doped silicon (donor -> extra free electron)'; svg.appendChild(label);
}

// Step 4: P-type doping (acceptor like Boron with 3 valence electrons) -> hole representation
function drawPdope() {
    clear(); drawLattice();
    const accX = 200 + 4 * 150; const accY = 140 + 1 * 130;
    const accCore = create('circle', { cx: accX, cy: accY, r: 18, class: 'acceptorAtom' });
    svg.appendChild(accCore);
    // hole visual: glowing ring that attracts an electron (animate neighbor electron moving in)
    const hole = create('circle', { cx: accX + 24, cy: accY - 12, r: 8, class: 'hole' });
    svg.appendChild(hole);
    // moving electron from nearby bond
    const startX = accX + 80, startY = accY + 30;
    const e = create('circle', { cx: startX, cy: startY, r: 6, class: 'electron' }); svg.appendChild(e);
    e.animate([{ transform: 'translate(0,0)' }, { transform: `translate(${accX - startX + 10}px,${accY - startY - 6}px)` }, { opacity: 0.12 }], { duration: 1500, fill: 'forwards' });
    const label = create('text', { x: W / 2, y: 40, 'text-anchor': 'middle', 'font-size': 16 }); label.textContent = 'P-doped silicon (acceptor -> hole created)'; svg.appendChild(label);
}

// wiring buttons
const btnAtom = document.getElementById('btn-atom'); const btnLattice = document.getElementById('btn-lattice'); const btnN = document.getElementById('btn-ndope'); const btnP = document.getElementById('btn-pdope'); const btnPlay = document.getElementById('btn-play');
function setActive(btn) { document.querySelectorAll('.controls button').forEach(b => b.classList.remove('active')); btn.classList.add('active'); }
btnAtom.onclick = () => { setActive(btnAtom); drawAtom(W / 2, 320, 1.1); };
btnLattice.onclick = () => { setActive(btnLattice); drawLattice(); };
btnN.onclick = () => { setActive(btnN); drawNdope(); };
btnP.onclick = () => { setActive(btnP); drawPdope(); };

// play sequence
btnPlay.onclick = async () => {
    btnAtom.click(); await wait(900);
    btnLattice.click(); await wait(1200);
    btnN.click(); await wait(1600);
    btnP.click();
};
function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

// initial
drawAtom(W / 2, 320, 1.1);